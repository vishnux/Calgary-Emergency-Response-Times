<h1 align="center">Optimizing Emergency Response Times in Calgary</h1>

<p align="center">
A Streamlit Dashboard designed to enhance emergency response operations across 300+ communities in Calgary.
</p>

## Executive Summary 

As cities expand and populations grow, ensuring efficient emergency response systems becomes increasingly vital. This project aims to address this pressing need by leveraging data analytics to enhance emergency services across the city. By simulating and analyzing the dynamics of emergency response, this project seeks to improve response times, ultimately saving lives and reducing property damage.

| **Service**          | **Suboptimal coverage level areas**                                                                                             | **Key Information**                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| EMS                   | Glacier Ridge, Legacy, Hotchkiss, and Wolf Willow          | Over 14% of communities fail to meet the response time target of 8 minutes and 59 seconds |
| Fire Station          | Glacier Ridge, Keystone Hills, Twin Hills, and Pegasus                   | Over 7% of communities fail to meet the response time target of 7 minutes |


The project recommends establishing additional stations and exploring cost-effective solutions, such as co-locating EMS stations within existing fire stations to address the significant disparities. EMS stations should be consolidated with fire stations at **11280 Valley Ridge Blvd NW**, **11920 Symons Valley Rd NW**, and **969 Walden Dr. SE**. This strategic alignment aims to enhance operational efficiency and effectiveness, offering substantial benefits for emergency response services.

> **Disclaimer:** These estimates are based on several assumptions and simulations. Actual response times may vary due to real-world factors such as traffic, weather conditions, and operational constraints.

## Execution 

1. Clone the repository

   ```
   $ git clone https://github.com/vishnux/Calgary-Emergency-Response-Times.git
   ```

2. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

3. Run the app

   ```
   $ streamlit run app.py
   ```

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Data Sources](#data-sources)
- [Real-World Factors](#real-world-factors)
- [Framework for Action](#framework-for-action)
- [Call to Action](#call-to-action)
- [License](#License)
- [Contact](#Contact)

## Overview

In emergencies, every second counts. The "Optimizing Emergency Response Times in Calgary" project focuses on mapping the paths and times taken by emergency vehicles, including fire trucks and ambulances, to reach their required destinations. By understanding how quickly emergency services can reach different parts of the city, we can identify areas where response times are slower and implement targeted improvements to Calgary's emergency response system.

## Key Features

- **Data-Driven Analysis**: Leveraging open data sources, including EMS and fire station locations, road networks, and community demographics, to inform our analysis.
- **Interactive Dashboard**: Providing stakeholders with an intuitive dashboard to visualize response times across different areas and make informed decisions.

## Data Sources

Our analysis incorporates various sources of data, including:

- [EMS station locations](https://data.calgary.ca/Health-and-Safety/EMS-Stations/s6f4-ijrf/data)
- [Fire station locations](https://data.calgary.ca/Health-and-Safety/Fire-Stations/cqsb-2hhg)
- [Addresses in Calgary](https://data.calgary.ca/Base-Maps/Parcel-Address/9zvu-p8uz/about_data)
- [Calgary roads](https://data.calgary.ca/Transportation-Transit/Neighbourhood-Speed-Limits/6qn4-9vc6/about_data)
- [Community demographics](https://data.calgary.ca/Base-Maps/Community-Points/j9ps-fyst)
- [City boundary](https://data.calgary.ca/Base-Maps/City-Boundary/erra-cqp9/about_data)

> Contains information licensed under the Open Government Licence — City of Calgary. License: https://data.calgary.ca/stories/s/u45n-7awa

## Real-World Factors

While our analysis provides valuable insights, it's essential to acknowledge real-world complexities such as:

- Traffic congestion
- Ambulance availability
- Prioritization of emergency calls
- Road closures and detours

## Framework for Action

Through meticulous data collection, analysis, and visualization, we've created a robust framework for assessing and improving emergency response times in Calgary. Our interactive dashboard offers stakeholders a comprehensive overview of response times, empowering them to make data-driven decisions and drive positive change.

## Call to Action

Optimizing emergency response times isn't just about data—it's about saving lives. We can build a safer and more resilient community by identifying opportunities for improvement and advocating for equitable access to emergency services. Together, let's work towards a future where every Calgarian can rely on swift and practical assistance in times of need.

## License

[Apache-2.0 license](https://choosealicense.com/licenses/apache-2.0/)

## Contact 

For inquiries or collaborations, please reach out [here](mailto:vishnurnair.official@gmail.com)
