   package zep

   import (
       "net/http"
   )

   func (c *ZepClient) Get(url string) (*http.Response, error) {
       return c.Client.Get(url)
   }

   func (c *ZepClient) Post(url string, bodyType string, body io.Reader) (*http.Response, error) {
       return c.Client.Post(url, bodyType, body)
   }

   // ... existing code ...