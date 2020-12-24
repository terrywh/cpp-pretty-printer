python
import sys
sys.path.insert(0, '/data/server/gcc-10.2/share/gcc-10.2.0/python')
sys.path.insert(0, '/data/htdocs/src/github.com/terrywh/gdb-pretty-printer/python')
end
## 
source /data/server/gcc-10.2/lib64/libstdc++.so.6.0.28-gdb.py
##
add-auto-load-safe-path /data/htdocs/src/github.com/terrywh/gdb-pretty-printer/gdb.py