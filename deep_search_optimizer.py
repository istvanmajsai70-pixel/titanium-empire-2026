import datetime

keywords = ["IT Enterprise Ecosystem", "Automated Profit 2026", "Titanium Empire Ultimate", "Passive Income Technology"]

def update_seo():
    today = datetime.date.today()
    meta_tags = f'<meta name="keywords" content="{", ".join(keywords)}">\n'
    meta_tags += f''
    
    try:
        with open("index.html", "r") as f:
            content = f.read()
        
        if "<head>" in content:
            updated_content = content.replace("<head>", f"<head>\n    {meta_tags}")
            with open("index.html", "w") as f:
                f.write(updated_content)
            print(f"[Deep Search] SEO kulcsszavak frissítve: {today}")
    except Exception as e:
        print(f"Hiba az SEO frissítés során: {e}")

if __name__ == "__main__":
    update_seo()
