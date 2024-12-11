# Makefile for Flask Random Forest App

# Define variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target
all: install

# Create virtual environment and install dependencies
install: $(VENV_DIR)/bin/activate
	@echo "Creating virtual environment and installing dependencies..."
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Installation complete."

# Run the Flask app
run: $(VENV_DIR)/bin/activate
	@echo "Running the Flask application..."
	FLASK_APP=app.py $(PYTHON) -m flask run

# Clean virtual environment and temporary files
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf $(VENV_DIR)
	@echo "Cleanup complete."

# Create the virtual environment if it doesn't exist
$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)

.PHONY: all install run clean
