##Tiny - The tiniest possible web framework. Inspired by [Flask](https://github.com/mitsuhiko/flask), [Bottle](https://github.com/bottlepy/bottle), and [Itty](https://github.com/toastdriven/itty/).

Example:

```python
import tiny

app = tiny.TinyApp()

@app.route('/')
def index():
    response = tiny.TinyResponse('Hello world')
    return response

tiny.run_app(app)
```


* To Do:
  1. ~~[Implement WSGI interface](https://github.com/jimjshields/tiny/commit/b41241cb2ca3b97bb86be41b81e23fb6e8c8abad)~~
  2. ~~[Parse HTTP GET request](https://github.com/jimjshields/tiny/commit/de0d595db7e0a8357fc504a6e3f19b2149d81eeb)~~
  3. ~~[Set up basic routing in request handler](https://github.com/jimjshields/tiny/commit/de0d595db7e0a8357fc504a6e3f19b2149d81eeb)~~
  4. ~~[Handle non-GET requests](https://github.com/jimjshields/tiny/commit/6ab7452ae689b0089dce8b9ea9619cc60f29d7c0)~~
  5. ~~[Parse queries more cleanly](https://github.com/jimjshields/tiny/commit/6ab7452ae689b0089dce8b9ea9619cc60f29d7c0)~~
  6. ~~[Handle requests more intelligently](https://github.com/jimjshields/tiny/commit/4e2fab42d38475eda23a68483b69ddda3b78e82b)~~
  7. ~~[Handle responses more intelligently](https://github.com/jimjshields/tiny/commit/4e2fab42d38475eda23a68483b69ddda3b78e82b)~~
  8. Move matching URLs into its own method
  9. ~~[Make decorator for creating URLs](https://github.com/jimjshields/tiny/commit/500eabf18e0cd0257d2a066d93fba1a81416aceb)~~
  10. Store HTTP statuses somewhere
  11. Generalize HTTP statuses/headers

* Overall Plan
  1. ~~[WSGI Server](https://github.com/jimjshields/tiny/commit/b41241cb2ca3b97bb86be41b81e23fb6e8c8abad)~~
  2. ~~[Request Handling](https://github.com/jimjshields/tiny/commit/4e2fab42d38475eda23a68483b69ddda3b78e82b)~~
  3. ~~[Response Handling](https://github.com/jimjshields/tiny/commit/4e2fab42d38475eda23a68483b69ddda3b78e82b)~~
  4. Routing
  5. Errors
  6. Tests