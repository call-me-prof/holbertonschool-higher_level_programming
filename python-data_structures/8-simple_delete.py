cat << 'EOF' > 8-simple_delete.py
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
EOF
chmod +x 8-simple_delete.py
