import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="your_package_name",
    version="your_version",
    author="author",
    author_email="email@domain.com",
    description="quick description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="your_url",
    download_url="your_download_url",
    include_package_data=True,
    install_requires=[],
    platforms="any",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)