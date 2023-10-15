   package zep

   import (
       "net/http"
   )

   type ZepClient struct {
       Client  *http.Client
       AClient *http.Client
   }

   func NewZepClient(client, aclient *http.Client) *ZepClient {
       return &ZepClient{
           Client:  client,
           AClient: aclient,
       }
   }