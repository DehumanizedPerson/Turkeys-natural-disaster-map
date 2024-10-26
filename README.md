# Turkish Natural Disaster Call API

---

## About The Project

The **Turkish Natural Disaster Call API** is designed to provide reliable information about natural disasters occurring within Turkey. By granting access to authenticated users, the API serves as a central, structured dataset for natural hazard information, including earthquakes, floods, fires, and more. This data source supports awareness and response to natural events, helping foster a safer and better-informed society.

## Motives

The primary goal of this project is to make natural disaster data more accessible, enabling individuals, organizations, and authorities to quickly retrieve crucial information. Turkey’s exposure to natural disasters, especially earthquakes, makes this initiative highly relevant. Key motives include:

- **Public Awareness**: Easy access to natural disaster information promotes safety and public awareness.
- **Reliable Information Access**: Centralizing disaster data reduces misinformation and provides a consistent resource for accurate information during crises.
- **Future Enhancements**: The API’s structure and codebase are designed with scalability in mind, allowing for future expansions and feature improvements.

## Usage Rights

The API is intended for public and institutional use by authorized users with API tokens. Usage rights are outlined as follows:

- **Open Access for Authorized Users**: Individuals, organizations, and government bodies with access can freely use the API.
- **Non-commercial and Commercial Use**: The API can be integrated into both non-commercial and commercial applications, provided that proper credit is given to the source.
- **Respect Rate Limits**: Users must adhere to set rate limits to ensure consistent access for all.
- **Data Accuracy and Liability**: While efforts are made to ensure data accuracy, it may not always be perfect. Users are responsible for interpreting and using the data responsibly.

## Code

The Turkish Natural Disaster Call API is divided into two main parts: the back-end (API) and the front-end (in progress). These components form the core functionality for accessing and retrieving disaster data.

### Back-End

The back-end of the Turkish Natural Disaster Call API (Version 0.1) is built using **FastAPI**, enabling secure, efficient, and asynchronous data retrieval. Key back-end features include token-based authentication, rate-limiting, and error handling to ensure reliability and ease of use.

#### Key Components

- **Token-based Authentication**: Only users with a valid API token can access data, enforced through the `validateToken` function.
- **Rate Limiting**: Each client is restricted to five requests per minute to prevent overuse and maintain system integrity, managed by **FastAPI’s RateLimiter**.
- **Error Handling**: Various error scenarios, such as invalid input or missing data, are handled to ensure reliable responses and aid in debugging.
