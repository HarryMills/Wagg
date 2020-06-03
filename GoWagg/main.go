package main

import (
	"Wagg/GoWagg/repl"
	"fmt"
	"os"
	"os/user"
)

func main() {
	person, err := user.Current()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Hello %s! This is the Wagg programming language!\n",
		person.Username)
	fmt.Printf("Feel free to type in commands\n")
	repl.Start(os.Stdin, os.Stdout)
}
