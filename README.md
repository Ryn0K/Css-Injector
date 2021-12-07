# Cross site scripting Injector (CSSI)

Tool to exfilterate tokens and nonces in websites, and can help to bypass client-side security.

###### I provided the [demo-labs](./demo-labs) ,vulnerable labs to show and try the working of this tool.

# Installation

- Install rustup : `curl https://sh.rustup.rs -sSf | sh`
- Install the nightly : `rustup install nightly`
- Default to nightly : `rustup default nightly`
- Build with cargo : `cargo build --release`

You will find build binary at **./target/release/cssi**

# Usage 

`./target/release/cssi --help`

```cssi 1.0
By Ryn0 (https://twitter.com/Ryn0K)
A tool to perform data exfilteration using css injection.

USAGE:
    cssi [OPTIONS] --template <template>

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information

OPTIONS:
        --ch <callback_host>     The address sic should use when calling callback endpoints. Must be different than the
                                 polling host. [default: http://localhost:3001]
    -c, --charset <charset>      Defines the list of possible characters that can be used in this token. [default:
                                 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]
        --ph <polling_host>      The address sic should use when calling polling endpoints. Must be different than the
                                 callback host. [default: http://localhost:3000]
    -p, --port <port>            Specifies the lower of two service instances that sic will spawn. For example, if 3000
                                 is specified, sic will spawn on 3000 and 3001. [default: 3000]
    -t, --template <template>    Points to a local file containing the css exfiltration template.
```

# Running Demo-labs : 

1. `cd demo-labs`
2. `docker-compose up`
3. than you can access vulnerable app [http://127.0.0.1:8886/](http://127.0.0.1:8886/).

##### Due to my tight schedule i will make documentation on this tool later.