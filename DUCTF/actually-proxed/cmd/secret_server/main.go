package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"github.com/davecgh/go-spew/spew"
)

var (
	port = flag.Int("port", 8081, "port to listen on")
)

func main() {

	flag.Parse()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("---------------------SERVER-------------------------")
		xff := r.Header.Values("X-Forwarded-For")

		ip := strings.Split(r.RemoteAddr, ":")[0]
		fmt.Println("-----------------------XFF---------------------------")
		spew.Dump(xff)
		fmt.Println("ip " + ip)
		if xff != nil {
			ips := strings.Split(xff[len(xff)-1], ", ")
			ip = ips[len(ips)-1]
			ip = strings.TrimSpace(ip)
		}

		// 1337 hax0rz 0nly!
		if ip != "31.33.33.7" {
			message := fmt.Sprintf("untrusted IP: %s", ip)
			http.Error(w, message, http.StatusForbidden)
			return
		} else {
			w.Write([]byte(os.Getenv("FLAG")))
		}
	})

	log.Printf("Listening on port %d", *port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
