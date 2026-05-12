import pandas as pd


# LEAD ANALYSIS FUNCTION

def analyze_lead(rating, website):

    try:
        rating = float(rating)

    except:
        rating = 0

    has_website = bool(website)

    # ==========================================
    # PREMIUM BUSINESS
    # ==========================================

    if rating >= 4.5:

        # HIGH RATING + WEBSITE
        if has_website:

            return {
                "website_present": "YES",
                "lead_type": "Premium Growth Client",
                "priority": "HIGH",
                "context": (
                    "Business already has strong ratings and online presence. "
                    "Best target for SEO, ads, automation, CRM and scaling services."
                )
            }

        # HIGH RATING + NO WEBSITE
        else:

            return {
                "website_present": "NO",
                "lead_type": "High Chance Website Client",
                "priority": "HIGH",
                "context": (
                    "Business has excellent ratings but no website. "
                    "Very strong opportunity for website development and online growth."
                )
            }

    # ==========================================
    # BEST POTENTIAL CLIENTS
    # ==========================================

    elif rating >= 3.5:

        return {
            "website_present": "YES" if has_website else "NO",
            "lead_type": "High Potential Client",
            "priority": "HIGH",
            "context": (
                "Business is very close to top-rated competitors. "
                "With review optimization, branding and local SEO, "
                "they can significantly improve visibility and conversions."
            )
        }

    # ==========================================
    # GROWTH OPPORTUNITY CLIENTS
    # ==========================================

    elif rating >= 3:

        return {
            "website_present": "YES" if has_website else "NO",
            "lead_type": "Growth Opportunity Client",
            "priority": "MEDIUM",
            "context": (
                "Business has growth potential but needs better reputation, "
                "marketing and customer trust improvements."
            )
        }

    # ==========================================
    # REPUTATION RECOVERY CLIENTS
    # ==========================================

    else:

        return {
            "website_present": "YES" if has_website else "NO",
            "lead_type": "Reputation Recovery Client",
            "priority": "MEDIUM",
            "context": (
                "Business needs reputation improvement and stronger online presence. "
                "Can benefit from review strategy, branding and better customer engagement."
            )
        }


# ==========================================
# SAMPLE RESULTS
# ==========================================

# results = [
#     {
#         "name": "Kendal Street Kitchen",
#         "phone": "+442039731903",
#         "rating": "4.8",
#         "url": "https://google.com/abc"
#     },

#     {
#         "name": "SCHOFIELD'S BAR",
#         "phone": "+447311777606",
#         "website": "https://example.com",
#         "rating": "4.7",
#         "url": "https://google.com/xyz"
#     }
# ]


# ==========================================
# FINAL EXCEL DATA
# ==========================================

def crete_lead_excel_file(results):
    excel_rows = []

    for item in results:
        print(item)
        rating = item.get("rating", "0")

        website = item.get("website", "")

        analysis = analyze_lead(
            rating,
            website
        )

        excel_rows.append({

            "Business Name": item.get("name",""),

            "Phone": item.get("phone", ""),

            "Website": website if website else "NO WEBSITE",

            "Website Present": analysis["website_present"],

            "Rating": rating,

            "Lead Type": analysis["lead_type"],

            "Priority": analysis["priority"],

            "Context": analysis["context"],

            "Google Maps URL": item.get("url", "")
        })


    # ==========================================
    # CREATE DATAFRAME
    # ==========================================

    df = pd.DataFrame(excel_rows)


    # ==========================================
    # EXPORT TO EXCEL
    # ==========================================

    output_file = "/home/shoarya/Desktop/leadomator/app/lead_report/google_maps_leads.xlsx"

    df.to_excel(output_file, index=False)


    print(f"Excel file saved: {output_file}")