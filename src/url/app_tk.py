import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from src.pe.predict_pe import predict_pe_file
from src.ui.predict_url import predict_url
from src.utils.scan import scan_folder

def on_scan_file():
    fp = filedialog.askopenfilename(
        title="Select PE file", 
        filetypes=[("PE files","*.exe *.dll *.sys"),("All files","*.*")]
    )
    if not fp: return
    res = predict_pe_file(fp)
    verdict = "MALWARE" if res["label"]==1 else "SAFE"
    messagebox.showinfo("PE Scan Result", f"File: {fp}\nVerdict: {verdict}\nProbability: {res['prob']:.3f}")

def on_scan_url():
    url = simpledialog.askstring("Scan URL", "Enter URL:")
    if not url: return
    res = predict_url(url)
    verdict = "MALICIOUS" if res["label"]==1 else "LEGIT"
    messagebox.showinfo("URL Scan Result", f"URL: {url}\nVerdict: {verdict}\nProbability: {res['prob']:.3f}")

def on_scan_folder():
    path = filedialog.askdirectory(title="Select folder to scan")
    if not path: return
    found = scan_folder(path)
    if not found:
        messagebox.showinfo("Folder Scan", "No PE files found.")
        return
    summary = "\n".join([f"{p}  ->  {'MALWARE' if lbl else 'SAFE'} ({prob:.3f})" for p,lbl,prob in found])
    messagebox.showinfo("Folder Scan Summary", summary)

def main():
    root = tk.Tk()
    root.title("XMalDetect — Desktop Malware Scanner")
    root.geometry("520x260")

    tk.Label(root, text="XMalDetect", font=("Segoe UI", 18, "bold")).pack(pady=10)
    tk.Button(root, text="Scan PE File", width=24, command=on_scan_file).pack(pady=6)
    tk.Button(root, text="Scan URL", width=24, command=on_scan_url).pack(pady=6)
    tk.Button(root, text="Scan Folder (simulate real-time)", width=24, command=on_scan_folder).pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    main()
