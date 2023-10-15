   package zep

   import (
       "fmt"
   )

   type APIError struct {
       Message string
   }

   func (e *APIError) Error() string {
       return fmt.Sprintf("API error: %s", e.Message)
   }

   func HandleResponse(response *http.Response) error {
       if response.StatusCode != 200 {
           return &APIError{Message: "Unexpected status code"}
       }
       return nil
   }