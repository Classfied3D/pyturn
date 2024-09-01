## 1. Install gopy Dependencies (Global)
* Make sure go is installed
* Edit `~/.bashrc`/`~/.zprofile`/other profile to include `export PATH="$PATH:$HOME/go/bin"`
* Download https://github.com/go-python/gopy from source
* Unzip, `cd` into that directory
* `go build && go install`
* `pip3 install build pybindgen wheel`
* Make sure to refresh the shell (close + open it)

## 2. Download Source + Install gopy Dependencies (Local)
* Download https://github.com/pion/turn/tree/master from source (from releases)
* Unzip, move the directory to the pyturn source directory, rename it to `turn`
* `cd` into the `turn` directory
* `go install github.com/go-python/gopy@latest`
* `go install golang.org/x/tools/cmd/goimports@latest`

## 3. Modify
* Add the contents of `injected.go` from the `// start injected.go` comment to `turn/client.go` (after it's imports)

## 4. Build
* `cd` into the `turn` directory
* `gopy build --output=pyturn -vm=python3 .`
* For me, the code produced had an error, where a parameter was named _, if this happens, follow these steps
  * Go to the file and line number which the error mentions in the `turn/pyturn` directory
  * This code references a variable with the name `_`, change this to `q` (or anything you want)
  * Now go to the function declaration in which also uses `_` as a parameter name, and replace this with what you named the variable in the previous step
  * Now run the previous command again while running `replace.py` (to prevent it overriding the file)
* Move `<src>/turn/pyturn` to `<src>/pyturn`

## 5. Modify
* Copy `__init__.py` to `pyturn/__init__.py`

## 6. Build
* (From the pyturn source directory) `python -m build -w .`

## 7. Install
* `pip3 install ` + the `.whl` file in `dist` (use `venv/bin/pip3` in a virtual environment)