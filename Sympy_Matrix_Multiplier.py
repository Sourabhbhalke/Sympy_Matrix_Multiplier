import streamlit as st
import sympy as sp

st.title("SymPy Matrix Calculator")

size = st.sidebar.radio("Matrix Size", [2, 3, 4, 5])
coeff_type = st.sidebar.radio("Coefficient Type", ["Whole", "Fraction"])

def create_matrix_input(size, coeff_type):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if coeff_type == "Fraction":
                value = st.number_input(f"Value at ({i+1},{j+1})", format="%.3f", step=0.01, key=f"{i}_{j}")
            else:
                value = st.number_input(f"Value at ({i+1},{j+1})", format="%d", step=1, key=f"{i}_{j}")
            row.append(value)
        matrix.append(row)
    return sp.Matrix(matrix)

matrix = create_matrix_input(size, coeff_type)

if st.button("Calculate"):
    st.write("Matrix:")
    st.write(matrix)
    
    try:
        inv_matrix = matrix.inv()
        st.write("Inverse Matrix:")
        st.write(inv_matrix)
    except:
        st.write("Matrix is not invertible.")
        
    det_matrix = matrix.det()
    st.write(f"Determinant: {det_matrix}")
    
    eigenvalues = matrix.eigenvals()
    st.write(f"Eigenvalues: {eigenvalues}")
