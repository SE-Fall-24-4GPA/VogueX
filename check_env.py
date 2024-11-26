import sys
import os


def check_environment():
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print("Python path:", sys.path)
    print("Current working directory:", os.getcwd())

    try:
        import chromadb
        print("ChromaDB version:", chromadb.__version__)
        print("ChromaDB location:", chromadb.__file__)
    except ImportError as e:
        print("ChromaDB import error:", str(e))

    try:
        import streamlit as st
        print("Streamlit version:", st.__version__)
        print("Streamlit location:", st.__file__)
    except ImportError as e:
        print("Streamlit import error:", str(e))


if __name__ == "__main__":
    check_environment()