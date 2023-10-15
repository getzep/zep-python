   package zep

   import (
       "net/http"
   )

   type MemoryClient struct {
       AClient *http.Client
       Client  *http.Client
   }

   func NewMemoryClient(aclient, client *http.Client) *MemoryClient {
       return &MemoryClient{
           AClient: aclient,
           Client:  client,
       }
   }

   // ... existing code ...