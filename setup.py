from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8-sig") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="heyrudra",
    version="1.0.0",
    author="Rudroneel Sengupta",
    author_email="11a.rudroneelsengupta@gmail.com",
    description="Natural language to shell command converter with AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nallanahaari/heyrudra",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "heyrudra=heyrudra.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "heyrudra": ["prompts/*.txt"],
    },
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    keywords="ai, cli, shell, commands, natural-language, automation",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/heyrudra/issues",
        "Source": "https://github.com/yourusername/heyrudra",
        "Documentation": "https://github.com/yourusername/heyrudra#readme",
    },
)