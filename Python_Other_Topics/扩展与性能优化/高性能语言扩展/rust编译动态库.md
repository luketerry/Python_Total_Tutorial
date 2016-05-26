
+ 先用cargo创建rust项目

        cargo new embed
        cd embed
        
+ 修改src/lib.rs


        use std::thread;

        #[no_mangle]
        pub extern fn process() {
            let handles: Vec<_> = (0..10).map(|_| {
                thread::spawn(|| {
                    let mut x = 0;
                    for _ in 0..5_000_000 {
                        x += 1
                    }
                    x
                })
            }).collect();

            for h in handles {
                println!("Thread finished with count={}",
                h.join().map_err(|_| "Could not join a thread!").unwrap());
            }
        }
        
        

`#[no_mangle]`
        `pub extern`
        
        
作为标签放在需要被引用的方法前

Cargo.toml文件:

    [package]
    name = "embed"
    version = "0.1.0"
    authors = ["HUANG SIZHE <hsz1273327@gmail.com>"]


    [lib]
    name = "embed"
    crate-type = ["dylib"]


```python
from ctypes import cdll
lib = cdll.LoadLibrary("embed/target/release/libembed.dylib")
lib.process()

print("done!")
```

    done!


我们来看看能提速多少

rust 代码

    #[no_mangle]
    pub extern fn fac(n:i32) ->i32 {

      if n<2 {
          return 1;
      } else{
      return n*fac(n-1);
      }
    }


```python

```
