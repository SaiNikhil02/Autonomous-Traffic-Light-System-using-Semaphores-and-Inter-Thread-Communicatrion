# Autonomous Traffic Light System

## Description

This project simulates an autonomous traffic light system that adjusts the timing of traffic lights based on real-time traffic conditions. The system uses semaphores to manage the flow of vehicles through intersections, ensuring efficient traffic management and minimal congestion.

## Key Concepts

- **Semaphores for Controlling Vehicle Flow**: Semaphores represent the traffic lights at intersections, controlling the flow of traffic.
- **Real-time Traffic Data Processing**: Simulate real-time traffic data using random vehicle generation and sensors.
- **Dynamic Adjustment of Traffic Light Timings**: Implement algorithms to dynamically adjust the green and red light durations based on current traffic conditions.

## Features

- Multiple producers (vehicles) and consumers (traffic lights) for realistic traffic simulation.
- Dynamic adjustment of traffic light timings based on traffic density.
- Use of semaphores and condition variables for synchronization.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/autonomous-traffic-light-system.git
    cd autonomous-traffic-light-system
    ```

2. Install the necessary Python packages (if any are required, typically threading is part of the standard library so no extra packages are needed).

## Usage

Run the main script to start the simulation:

```bash
python main.py
## Project Structure
main.py: Main execution script that runs the traffic light simulation and vehicle generation.
traffic_light.py: Contains the TrafficLight and DynamicTrafficLight classes for managing traffic lights.
intersection.py: Contains the Intersection class to manage the intersection logic.
vehicle.py: Contains the Vehicle class for simulating vehicles.

License
This project is licensed under the MIT License - see the LICENSE file for details.
