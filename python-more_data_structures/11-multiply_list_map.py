cat << 'EOF' > 11-multiply_list_map.py
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
EOF
