   package zep

   import (
       "net/http"
   )

   type UserClient struct {
       AClient *http.Client
       Client  *http.Client
   }

   func NewUserClient(aclient, client *http.Client) *UserClient {
       return &UserClient{
           AClient: aclient,
           Client:  client,
       }
   }

   // ... existing code ...