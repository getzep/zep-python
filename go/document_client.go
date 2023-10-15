   package zep

   import (
       "net/http"
   )

   type DocumentClient struct {
       AClient *http.Client
       Client  *http.Client
   }

   func NewDocumentClient(aclient, client *http.Client) *DocumentClient {
       return &DocumentClient{
           AClient: aclient,
           Client:  client,
       }
   }

   // ... existing code ...