   package main

   import (
       "net/http"
       "zep"
   )

   func main() {
       client := &http.Client{}
       zepClient := zep.NewZepClient(client, client)
       // ... existing code ...
   }