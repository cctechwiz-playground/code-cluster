package main

import (
    "fmt"
    "log"
    "github.com/boltdb/bolt"
)

func main(){
    db, err := bolt.Open("/home/josh/Documents/AFL_convert/crashwalk.db", 0644, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    fmt.Println("Hello world")

    err = db.View(func(tx *bolt.Tx) error {
        bucket := tx.Bucket([]byte("crashes"))
        fmt.Println("Bucket %s", bucket)
        if err := bucket.ForEach(func(k, v []byte) error {
            fmt.Println("k:%s v:%s", k, v)
            return nil
        }); err != nil {
            return err
        }
        return nil
    })

    if err != nil {
        log.Fatal(err)
    }

    if err := db.Close(); err != nil {
        log.Fatal(err)
    }
}
