cat << 'EOF' > 6-print_sorted_dictionary.py
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
EOF
chmod +x 6-print_sorted_dictionary.py
