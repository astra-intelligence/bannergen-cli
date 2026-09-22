from setuptools import setup, find_packages

setup(
    name="bannergen-cli",
    version="0.1.0",
    description="AI-powered social media banner generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adventure Agent",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    extras_require={
        "overlay": ["Pillow>=10.0.0"],
    },
    entry_points={
        "console_scripts": [
            "bannergen=bannergen.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)