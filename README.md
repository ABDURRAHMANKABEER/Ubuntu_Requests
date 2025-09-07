# Ubuntu_Requests
# Ubuntu Image Fetcher  

> *"I am because we are."* – Ubuntu Philosophy  

Ubuntu Image Fetcher is a Python tool for respectfully collecting images from the web.  
It reflects the spirit of Ubuntu: **community, respect, and sharing**.  

## ✨ Features
- Fetches one or multiple images from user-provided URLs.  
- Creates a `Fetched_Images` directory automatically if it doesn’t exist.  
- Handles network and HTTP errors gracefully.  
- Prevents duplicate files by renaming images automatically.  
- Organizes downloads for later sharing and appreciation.  

## 📂 Project Structure
```
Ubuntu_Requests/
│
├── Fetched_Images/    # Saved images will appear here
├── fetcher.py         # Main Python script
└── README.md          # Documentation
```

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Ubuntu_Requests.git
   cd Ubuntu_Requests
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Run the script:
   ```bash
   python fetcher.py
   ```

4. Enter one or multiple image URLs (comma-separated). Example:
   ```
   Please enter image URLs (separated by commas): 
   https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png, https://www.python.org/static/community_logos/python-logo.png
   ```

5. Output example:
   ```
   ✓ Successfully fetched: Tux.png
   ✓ Image saved to Fetched_Images/Tux.png
   ✓ Successfully fetched: python-logo.png
   ✓ Image saved to Fetched_Images/python-logo.png

   Connection strengthened. Community enriched.
   ```

## 🛡️ Error Handling
- Invalid URL format → friendly error message.  
- Connection issues → script won’t crash, it will notify user.  
- Duplicate filenames → automatically renamed (`image_1.jpg`, `image_2.jpg`).  
- Timeout → script retries gracefully.  

## 🌍 Ubuntu Principles
- **Community:** Connects with the global web to share resources.  
- **Respect:** Handles failures without crashing.  
- **Sharing:** Saves images neatly for later appreciation.  
- **Practicality:** A real tool for collecting and organizing images.  

---

**A person is a person through other persons.**  
Ubuntu Image Fetcher connects you to the creativity and generosity of the web community.  
