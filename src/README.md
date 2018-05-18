# Django Congress JP 2018 の資料中で使用したソースコード

このディレクトリ以下に含まれるソースコードは

- WSGIアプリ ( `wsgi_app` 以下)
- Djangoアプリ ( `myproject` 以下)

の2種類です。

以下にアプリの起動方法を記載します。

　  

---

## WSGIアプリ

`src/wsgi_app` ディレクトリの中で起動


### 関数ベースのWSGIアプリの起動と動作確認

起動

```
$ python server_using_function.py 
```

動作確認

```
$ curl http://localhost:15000
Hello, WSGI function
```

　  
### クラスベースのWSGIアプリの起動と動作確認

起動

```
$ python server_using_class.py 
Serving on port 15001...
```

動作確認

```
$ curl http://localhost:15001
Hello, WSGI class
```

　  
### WSGIアプリ + WSGIミドルウェアの起動と動作確認

起動

```
$ python server_using_class_with_middleware.py 
Serving on port 15002...
```

動作確認

```
$ curl http://localhost:15002
Hello, WSGI class
Hello, WSGI middleware
```

　  

---

## Djangoアプリ

### WSGIミドルウェアとDjangoアプリ

#### 起動

```
$ python manage.py runserver --settings=myproject.settings.wsgi
```

#### 動作確認
##### curl

```
$ curl http://localhost:8000/myapp/hello
Hello world
```

##### Djangoログ

```
[wsgi_middleware] before view
called: HelloView
[wsgi_middleware] after view
```

　  
### HelloDjangoMiddleware

#### 起動

```
$ python manage.py runserver --settings=myproject.settings.hello
```

#### 動作確認
##### curl

```
$ curl http://localhost:8000/myapp/hello
Hello world
```

##### Djangoログ

```
[hello] one-time configuration
[hello] before view
called: HelloView
[hello] after view
```

　  
### ProcessViewDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.process_view
```

#### 動作確認
#####  クエリ文字列fooがある場合

###### curl

```
$ curl localhost:8000/myapp/hello?foo=123
Hello world
```

###### Djangoログ

```
[process_view] before view
[process_view] hook!
called: HelloView
[process_view] after view
```


##### クエリ文字列fooが無い場合
###### curl

```
$ curl localhost:8000/myapp/hello?bar=456
overwrite by process_view
```

###### Djangoログ

```
[process_view] before view
[process_view] hook!
[process_view] after view
```

　  
### ProcessTemplateResponseDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.process_template_response
```

#### 動作確認
##### curl

```
$ curl localhost:8000/myapp/template
overwrite by middleware
```

##### Djangoログ

```
[process_template_response] before view
called: HelloTemplateView
[process_template_response] hook!
[process_template_response] after view
```

　  
### ProcessViewTemplateDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.process_view_template
```

#### 動作確認

```
[process_view] before view
[process_view] hook!
<class 'django.core.handlers.wsgi.WSGIRequest'>
<class 'function'>
<class 'tuple'>
<class 'dict'>
[process_template_response] hook!
<class 'django.core.handlers.wsgi.WSGIRequest'>
<class 'django.template.response.TemplateResponse'>
[process_view] after view
```

### ProcessExceptionDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.process_exception
```

#### 動作確認
##### クエリ文字列 `http` がある場合
###### curl

```
$ curl localhost:8000/myapp/error?http=0
HttpResponse by process_exception
```

###### Djangoログ

```
[process_exception] before view
called: ExceptionView
[process_exception] hook!
[process_exception] return HttpResponse
[process_exception] after view
```


##### クエリ文字列 `template` がある場合 
###### curl

```
$ curl localhost:8000/myapp/error?template=0
TemplateResponse by process_exception
called process_template_response
```

###### Djangoログ

```
[process_exception] before view
called: ExceptionView
[process_exception] hook!
[process_exception] return TemplateResponse
[process_exception] hook by template response
[process_exception] after view
```


##### クエリ文字列が無い場合
###### curl

```
$ curl localhost:8000/myapp/error
...
<title>ValueError at /myapp/error</title>
...
```

###### Djangoログ

```
Internal Server Error: /myapp/error
Traceback (most recent call last):
...
    raise ValueError('Oops!')
ValueError: Oops!
```

　  
### DeprecationMixinDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.deprecation
```

#### curl

```
$ curl localhost:8000/myapp/template
overwrite by deprecation mixin middleware
```

　  
### UnusedDjangoMiddleware
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.unused
```


#### 実行結果
##### curl

```
$ curl localhost:8000/myapp/template
hello
```

##### Djangoログ

```
[unused] one-time configuration
called: HelloTemplateView
```

　  
### 複数WSGIミドルウェア(FirstWSGIMiddleware他)
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.multi_wsgi_middleware
```

#### Djangoログ

```
[wsgi1] before view
[wsgi2] before view
[wsgi3] before view
called: HelloTemplateView
[wsgi3] after view
[wsgi2] after view
[wsgi1] after view
```

　  
### 複数Djangoミドルウェア(FirstDjangoMiddleware他)
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.multi_django_middleware
```

#### Djangoログ

```
[django3] one-time configuration
[django2] one-time configuration
[django1] one-time configuration
[django1] before view
[django2] before view
[django3] before view
[django1] process view
[django2] process view
[django3] process view
called: HelloTemplateView
[django3] process template response
[django2] process template response
[django1] process template response
[django3] after view
[django2] after view
[django1] after view
```

　  
### Django/WSGIミドルウェアとも複数ある場合
#### 起動

```
$ python manage.py runserver --settings=myproject.settings.multi_wsgi_and_django_middleware
```


#### Djangoログ

```
[django2] one-time configuration
[django1] one-time configuration
[wsgi1] before view
[wsgi2] before view
[django1] before view
[django2] before view
[django1] process view
[django2] process view
called: HelloTemplateView
[django2] process template response
[django1] process template response
[django2] after view
[django1] after view
[wsgi2] after view
[wsgi1] after view
```

　  
### WSGIミドルウェアでの例外送出
#### WSGIミドルウェアでハンドリング
##### 起動

```
$ python manage.py runserver --settings=myproject.settings.handling_exception_by_wsgi_and_django
```

##### curl

```
$ curl localhost:8000/myapp/template
# Djangoのエラーページ
```

##### Djangoログ

```
[template] process template response
Internal Server Error: /myapp/template
...
ValueError: raised by process_template_response
[wsgi] response: <class 'django.http.response.HttpResponse'>
```

　  
### Djangoミドルウェアで例外送出

#### Djangoミドルウェアでハンドリング
##### 起動
###### `__call__()` で例外送出

```
$ python manage.py runserver --settings=myproject.settings.handling_exception_by_call
```

###### `process_view()` で例外送出

```
$ python manage.py runserver --settings=myproject.settings.handling_exception_by_process_view
```

###### `process_template_response()` で例外送出

```
$ python manage.py runserver --settings=myproject.settings.handling_exception_by_process_template_response
```

###### `process_exception()` で例外送出

```
$ python manage.py runserver --settings=myproject.settings.handling_exception_by_process_exception
```
