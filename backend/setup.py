from setuptools import setup, find_packages

setup(
    name="riqa_software",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-socketio',
        'python-dotenv',
        'numpy'
    ],
    python_requires='>=3.6',
)
