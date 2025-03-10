# Test Clean Architecture Implementation

This project demonstrates the implementation of Clean Architecture in a software application. Clean Architecture is a design pattern that promotes separation of concerns, making the system more maintainable, testable, and scalable.

## Project Structure

The project is divided into several layers:
- **Domain**: Contains the core business logic and entities.
- **Application**: Contains use cases and service interfaces.
- **Infrastructure**: Contains implementations of the service interfaces, data access, and external APIs.
- **Presentation**: Contains the user interface and controllers.

## How It Works

1. **Domain Layer**: Defines the core entities and business rules.
2. **Application Layer**: Implements the use cases and interacts with the domain layer.
3. **Infrastructure Layer**: Provides concrete implementations for data access and external services.
4. **Presentation Layer**: Handles user interactions and presents data to the user.

- For this project I've selected to implement it for bank management's "Account" entity. As discussed above
 this entity will have its own actions, use case, interface adapters and controller all in which are included in a separate folders (or layers if we're being technical). The file structure looks like this:

 ```
 |- entities
 |      |---- account.py
 |- interface_adapters
 |      |----account_repository.py
 |- use_cases
 |      |----transfer_funds.py
 |- tests
 |      |----test_account.py
 |      |----test_in_memory_account_repository.py
 |      |----test_transfer_funds.py
 |- main.py
 ```

## Prerequisites

To run this project, you will need:

- Python 3.10 or above
- A code editor like Visual Studio Code or Visual Studio (or Vim if your more of a terminal fan)
- Git for version control

Make sure you have these installed and properly configured on your machine.

## Running the Application

1. Clone the repository:
    ```sh
    git clone https://github.com/blackhammer116/Test-Clean-architecture-implemtation.git
    cd Test-Clean-architecture-implementation
    ```

2. install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the main file:
    ```sh
    python main.py
    ```
    

## Running the Tests

1. Navigate to the root of the project directory

2. Run the tests:
    ```sh
    pytest tests/
    ```

