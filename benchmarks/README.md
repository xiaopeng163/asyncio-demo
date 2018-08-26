# Benchmark for Http Server


## setup

Install requirements

```bash
pip install -r requirements.txt
```

Install wrk [Modern HTTP benchmarking tool](https://github.com/wg/wrk)

On Mac, just

```bash
brew install wrk
```

## Start all http server


```bash
python asyncio_http.py
```

```bash
export FLASK_APP=flask_http.py
flask run
```

```bash
python tornado_http.py
```

## Results

```bash
➜  ~ wrk -t12 -c400 -d30s http://127.0.0.1:8888/100
Running 30s test @ http://127.0.0.1:8888/100
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   180.27ms   32.94ms 329.64ms   89.84%
    Req/Sec   173.31     49.03   303.00     69.16%
  62217 requests in 30.10s, 17.44MB read
  Socket errors: connect 0, read 381, write 0, timeout 0
Requests/sec:   2067.11
Transfer/sec:    593.49KB
➜  ~ wrk -t12 -c400 -d30s http://127.0.0.1:5000/100
Running 30s test @ http://127.0.0.1:5000/100
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   162.54ms   77.98ms 422.78ms   72.48%
    Req/Sec    61.26     41.97   310.00     77.66%
  15643 requests in 30.09s, 3.80MB read
  Socket errors: connect 0, read 1780, write 6, timeout 0
Requests/sec:    519.88
Transfer/sec:    129.46KB
➜  ~ wrk -t12 -c400 -d30s http://127.0.0.1:25000/100
Running 30s test @ http://127.0.0.1:25000/100
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.94ms    2.95ms  57.08ms   86.00%
    Req/Sec     2.01k   259.08     3.32k    88.75%
  720726 requests in 30.07s, 114.10MB read
  Socket errors: connect 0, read 302, write 0, timeout 0
Requests/sec:  23965.96
Transfer/sec:      3.79MB
```


## Links

[uvloop: Blazing fast Python networking](https://magic.io/blog/uvloop-blazing-fast-python-networking/)

