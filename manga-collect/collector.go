package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"path/filepath"

	"github.com/ChimeraCoder/anaconda"
	"github.com/joho/godotenv"
)

func main() {
	//Twitter認証

	n := godotenv.Load()
	if n != nil {
		fmt.Println("not found api key")
	}

	consumerKey := os.Getenv("ConsumerKey")
	consumerSecret := os.Getenv("ConsumerSecret")
	accessToken := os.Getenv("AccessToken")
	accessTokenSecret := os.Getenv("AccessTokenSecret")

	anaconda.SetConsumerKey(consumerKey)
	anaconda.SetConsumerSecret(consumerSecret)

	//個人認証
	api := anaconda.NewTwitterApi(accessToken, accessTokenSecret)

	fmt.Println("検索クエリを入力")
	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()
	text := stdin.Text()

	//検索クエリの設定
	v := url.Values{}
	v.Set("count", "5")
	query := text + "exclude:retweets filter:images"
	searchResult, _ := api.GetSearch(query, v)

	//画像を保存するフォルダの作成・ディレクトリ移動

	currentDir, err := filepath.Abs(".")
	if err != nil {
		panic(err)
	}

	_, err = os.Stat(text)
	if err != nil {
		err = os.Mkdir(text, 0777)
		if err != nil {
			panic(err)
		}
	}

	err = os.Chdir(currentDir + "/" + text)
	if err != nil {
		panic(err)
	}

	//ツイートをクローリングして、画像を取得

	for i, tweet := range searchResult.Statuses {
		mediaRawURL := tweet.ExtendedEntities.Media[0].Media_url_https

		response, err := http.Get(mediaRawURL)
		if err != nil {
			panic(err)
		}
		defer response.Body.Close()

		images, err := os.Create(fmt.Sprintf("images%d.jpg", i))
		if err != nil {
			panic(err)
		}
		defer images.Close()

		io.Copy(images, response.Body)
	}
}
