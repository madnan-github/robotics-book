# Use ROS 2 Humble Hawksbill with Ubuntu 22.04
FROM ros:humble

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements if available (we'll create this later)
COPY requirements.txt /app/requirements.txt

# Install Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Source ROS 2 environment
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN source /opt/ros/humble/setup.bash

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app:$PYTHONPATH
ENV ROS_DOMAIN_ID=0

# Expose port for Docusaurus (if needed)
EXPOSE 3000

# Default command
CMD ["bash"]