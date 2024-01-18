# ASSERT: AI-Supported Smart Electricity Restoration Tool

## Pitch

ASSERT is a data-driven GIS solution designed to assist directors of Utility Emergency Response Teams (UERTs) in efficiently deploying resources during power outages and streamlining grid restoration efforts. Our inspiration stems from extensive user research, as well as pin-pointing hurdles in current datasets such as ODIN being very sporadic. 

By noticing trends in various Census Data, Social Vulnerability Data, and Power Outage Data, we were able to train an algorithm to predict the vulnerability of different counties' eectrical-outage vulnerability. Thus, in the event of  power outage, a UERT will know the counties which are more overburdned by Electrical Outages, and thus send more resources that way.

### Why ASSERT?

Power outages are inevitable, and the key to effective response lies in predicting outage impact and allocating resources accordingly. ASSERT leverages federal open data and advanced regression models to address this challenge. We used the following datasets: 

- CDC/ATSDR Social Vulerability Indices: https://www.atsdr.cdc.gov/placeandhealth/svi/index.html
- Outage Data Initiative power outage dataset: https://odin.ornl.gov/

This project was completed under "The Opportunity Project" Sprint, organized by U.S. Census Bureau, and our project was done in partnership with The Department of Energy. More details on the sprint can be found here: https://opportunity.census.gov/

## Target Audience

Directors of Utility Emergency Response Teams (UERTs) are the primary users of ASSERT. Examples include National Grid, Eversource, AAA, etc. These professionals play a crucial role in managing resource deployment and grid restoration in the aftermath of power outages.

## User Experience Advocates

We extend our sincere gratitude to the following User Experience Advocates who generously shared their invaluable insights and expertise, contributing significantly to the success of ASSERT:

- [Carol Freeman](https://www.linkedin.com/in/carol-freeman/) — National Preparedness Analytics Center, Argonne National Laboratory
- [Scott Sternfeld](https://www.linkedin.com/in/scottsternfeld/) — The Outage Data Initiative
- [Hessann Farooqi](https://bostoncan.org/hessann-farooqi/) — Boston Climate Action Network
- [Kristen Finne](https://www.linkedin.com/in/kristen-finne-a643979/) — Department of Health and Human Services
- [Jason Eisdorfer](https://www.linkedin.com/in/jason-eisdorfer-9613555/) — Pacific Northwest National Lab
- [Todd Levin](https://www.anl.gov/profile/todd-levin) — Argonne National Laboratory

Their unwavering commitment and insights have played a crucial role in refining the product and ensuring its relevance to real-world scenarios.

## Next Steps

We are in the process of having utilities test the ASSERT product to identify areas of improvement and ensure its effectiveness in real-world scenarios. 

We are also in the process of creating developer documentation such that this repository can be opened for further contribution. 

We are improving the website's other pages to make the product self-contained, i.e. make it such that a user can surf around the website and infer every detail behind datasets, the product itself, and download our datasets. Currently, the datasets are located under the ```main``` branch, ```data``` directory.

One key area for improvement is understanding which social vulnerability indicators are most significant for predicting power outage impact. Exploring different regression models will further enhance the accuracy of ASSERT's predictions.

## Information about ASSERT

### 1) Identify Your End User

Our end users are directors of Utility Emergency Response Teams (UERTs) responsible for resource deployment and grid restoration during power outages.

### 2) User Advocates

Throughout the sprint, we collaborated with user advocates such as Carol Freeman, Scott Sternfeld, Hessann Farooqi, Kristen Finne, Jason Eisdorfer, and Todd Levin.

### 3) Federal Open Data Used

We utilized the CDC/ATSDR Social Vulnerability Indices dataset and the Outage Data Initiative power outage dataset as our primary sources of federal open data.

### 4) Overview of What We Built

We used the SVI and ODIN datasets to build ASSERT, a solution that aids in determining resource allocation for electric utility distribution during power outages.

### 5) Key Metrics for Tracking Usage and Impact

To measure the effectiveness of ASSERT, we plan to ask end users questions such as:
- Is ASSERT easy to use?
- Is the purpose of ASSERT clear?
- Does ASSERT help you do your job?
- What is your favorite feature of ASSERT?
- What's the one aspect of ASSERT that needs the most improvement?

### 6) General User Journey

Imagine being a UERT in charge of managing resources for a state with limited outage data. ASSERT helps predict energy burden, facilitating the prioritization of counties in restoration efforts.

### 7) Deployment/Implementation Plan

ASSERT will be deployed via GitHub Pages and as a Leaflet GIS application. Our model, based on regression analysis, considers factors like unemployment per capita, percent minority populations, and people below 150% of the poverty estimate. We used the entire ODIN dataset to form the regression model and made predictions for counties not covered by ODIN.

## Open Source Repository

The open-source repository for all datasets and website code for ASSERT is currently being cleaned up.

```plaintext
ASSERT: AI-Supported Smart Electricity Restoration Tool
Copyright (C) 2023 UMass iCons (Anvitha Ramachandran, Gabby Walczak, Jose Cruz Mendez,
                                Kushagra Srivastava, Sarojini Torchon, Scott Auerbach,
                                Suhani Chawla, Sophie Auerbach)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

```

“Free software” means software that respects users' freedom and community. Roughly, it means that the users have the freedom to run, copy, distribute, study, change and improve the software. Thus, “free software” is a matter of liberty, not price. To understand the concept, you should think of “free” as in “free speech,” not as in “free beer.” We sometimes call it “libre software,” borrowing the French or Spanish word for “free” as in freedom, to show we do not mean the software is gratis.

ASSERT is a crucial program addressing the impact of power outages, and making it free software serves several purposes:
- **Community Collaboration:** Libre source encourages collaboration, allowing experts and communities to contribute to the improvement and development of ASSERT.
- **Transparency:** The transparency of libre source fosters trust among users and stakeholders. They can inspect, modify, and understand the code, ensuring the integrity of the tool. Crucially, Libre source ensures that any derivatives of the product should remain libre & open (including sources), and not be obscured & proprietarized.
- **Accessibility:** By making ASSERT open source, we ensure that the tool is accessible to a wider audience, promoting inclusivity and the democratization of technology.

You may have paid money to get copies of a free program, or you may have obtained copies at no charge. But regardless of how you got your copies, you always have the freedom to copy and change the software, even to sell copies.

With love, 

The UMass iCons Team for The 2023 Opportunity Project.
