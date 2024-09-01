* Make sure go is installed
* Edit `~/.bashrc`/`~/.zprofile`/other profile to include `export PATH="$PATH:$HOME/go/bin"`
* Download https://github.com/go-python/gopy from source
* Unzip, `cd` into that directory
* `go build && go install`
* `pip3 install pybindgen wheel`
* Make sure to refresh the shell (close + open it)
* Download https://github.com/pion/turn/tree/master from source
* Unzip, move the directory to the folder containing this file, `cd` into that directory
* `go install github.com/go-python/gopy@latest`
* `go install golang.org/x/tools/cmd/goimports@latest`
* `gopy build --output=../pyturn -vm=python3 .`
* For me, the code produced had an error, where a parameter was named _, if this happens, follow these steps
  * Go to the file and line number which the error mentions in the `pyturn` directory
  * This code references a variable with the name `_`, change this to `q` (or whatever)
  * Now go to the function declaration in which also uses `_` and replace this with what you named the variable in the previous step
  * Now run `replace.py` while running the previous command again (to prevent it overriding the file), then stop `replace.py`
* `cd` to the folder containing this file
* `python3 setup.py bdist_wheel`
* `wheel_file=$(ls dist/*.whl | head -n1); pip3 install $wheel_file`