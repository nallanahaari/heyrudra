# HeyRudra

**Natural Language to Shell Command Converter with AI Agents**

Convert your natural language instructions into safe, executable shell commands with intelligent commit message generation.

## Tech Stack 
1. **LangGraph**
2. **Redis**
3. **SubProcesses**

## Features

- 🤖 **AI-Powered Command Generation** - Uses GPT-4 to understand natural language
- 🛡️ **Safety Verification** - Blocks dangerous commands and warns about risky ones
- 💬 **Smart Commit Messages** - Automatically generates contextual commit messages from git diffs
- 📁 **Session Management** - Tracks current working directory across commands
- ⚡ **Command Caching** - Caches commands using Redis for faster execution
- 🔄 **Multi-step Workflows** - Handles complex multi-command operations

##  Quick Start

### Installation

```bash
# Install from source
git clone https://github.com/nallanahaari/heyrudra.git
cd heyrudra
pip install -e .


```

### Setup

1. **Set your OpenAI API key:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

2. **Start Redis (for caching):**
```bash
docker run -d -p 6379:6379 --name redis-server redis
```

### Usage

```bash
# Basic file operations
heyrudra "create a new folder called test"
heyrudra "show me the files in this directory"
heyrudra "copy setup.py to backup folder"

# Git operations with smart commit messages
heyrudra "commit my changes"
heyrudra "push to master branch"
heyrudra "create a new branch feature-auth"

# Directory navigation
heyrudra "go to the parent directory"
heyrudra "change to the src folder"

# Package management
heyrudra "install the requests library"
heyrudra "update all pip packages"
```

##  Examples

### Smart Git Commit Messages

Instead of generic messages like "update file.py", HeyRudra analyzes your actual code changes:

```bash
# Make some changes to your code
echo "def validate_email(email): return '@' in email" >> utils.py

# Commit with intelligent message generation
heyrudra "commit this new validation function"
# Result: "feat(utils): add validate_email function"
```

### Safety Features

HeyRudra protects you from dangerous commands:

```bash
heyrudra "delete everything in the system"
# Result: 🚫 Command blocked: Attempting to delete root directory
```

### Multi-step Operations

Handle complex workflows in one command:

```bash
heyrudra "stage all changes, commit with proper message, and push to main"
# Result: Executes git add ., generates commit message, and pushes
```

##  Architecture

HeyRudra uses a multi-agent architecture with LangGraph:

1. **Planner Agent** - Analyzes intent and determines task type
2. **Command Generator** - Converts natural language to shell commands
3. **Commit Message Agent** - Generates contextual commit messages from git diffs
4. **Verifier Agent** - Performs safety checks and validates commands
5. **Executor Agent** - Safely executes commands and captures output

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/nallanahaari/heyrudra.git
cd heyrudra

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black heyrudra/
flake8 heyrudra/
```

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Redis server (for caching)
- Git (for commit message generation)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-amazing`)
3. Commit your changes (`heyrudra "commit my amazing feature"` 😉)
4. Push to the branch (`git push origin feature-amazing`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for the GPT-4 API
- LangChain team for the LangGraph framework
- Redis for caching infrastructure

---

**Made with ❤️ for developers who love natural language interfaces (ahem, struggle with cmd)**