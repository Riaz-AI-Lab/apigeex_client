from setuptools import setup, find_packages

setup(
    name="apigeex_client",
    version="0.1.0",
    author="Phu Tran",
    author_email="tran.phu@mayo.edu",
    description="Universal APIGEE X Client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tranngocphu/apigeex_client",
    packages=find_packages(exclude=["tests*", "docs"]),
    install_requires=[
        "attrs",
        "httpx",
        "openapi_python_client",
        "python-dotenv",
        "python_dateutil",
        "pyyaml",
        "requests",
    ],
    python_requires=">=3.7",
)
