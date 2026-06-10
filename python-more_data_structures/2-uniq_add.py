cat << 'EOF' > 2-uniq_add.py
#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(set(my_list))
EOF
