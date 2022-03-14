import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stream-finder",
    version="0.0.1",
    author="Debangshu Chakraborty",
    author_email="code.debangshu@gmail.com",
    description="A python API to find streaming sources of any movie or television show",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Debangshu-Chakraborty/stream-finder.git",
    #project_urls={
    #    "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
