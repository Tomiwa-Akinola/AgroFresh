AgroFresh

AgroFresh is a web-based platform for buying and selling food products. It enables users to list items, engage in conversations, and manage their accounts through a user-friendly dashboard.

Features
- User Registration and Authentication: Users can sign up, log in, and manage their profiles.
- Item Listings: Users can list agricultural items for sale, complete with descriptions and images.
- Conversations: Buyers and sellers can communicate through an integrated messaging system.
- Dashboard: Each user has access to a dashboard where they can view and manage their listings and conversations.

Technologies Used

- Backend: Python(Django)
  
- Frontend: HTML, CSS, and Django Templates


Project Structure

- AgroFresh/: Main project folder containing settings, URLs, and configurations.
- conversation/: Handles the messaging feature between users.
- core/: Contains base functionality and site-wide configurations.
- dashboard/: Manages the user dashboard, where users can control their interactions and listings.
- item/: Manages the item listing feature.
- media/: Stores user-uploaded files, such as item images.

## Installation

To set up the project locally on bash, follow these steps:

1. Clone the repository:
   git clone https://github.com/Tomiwa-Akinola/AgroFresh.git
   cd AgroFresh

2. Create a virtual environment and activate it:
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Run the development server:
   python manage.py runserver

6. Access the project:
   Open your browser and go to `http://127.0.0.1:8000`.

Usage

- After installation, you can register as a user, add food items for sale, and interact with other users via the conversation system.

Contributing

If you would like to contribute to AgroFresh, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

