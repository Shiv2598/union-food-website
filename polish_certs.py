with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Image 3 Certifications Seals Polish */
.cert-badge-item {
  width: 86px !important;
  height: 86px !important;
  object-fit: contain !important;
  background: #ffffff !important;
  border-radius: 50% !important;
  padding: 4px !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08) !important;
  border: 1px solid rgba(0, 0, 0, 0.04) !important;
  transition: transform var(--transition-base), box-shadow var(--transition-base) !important;
}
.cert-badge-item:hover {
  transform: scale(1.12) !important;
  box-shadow: 0 8px 22px rgba(0, 0, 0, 0.16) !important;
}
''')
print("Appended cert badge polish to css/style.css")
