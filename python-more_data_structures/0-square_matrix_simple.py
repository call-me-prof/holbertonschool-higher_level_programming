cat << 'EOF' > 0-square_matrix_simple.py
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]
EOF
