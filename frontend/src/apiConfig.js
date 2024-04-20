const ENV = "prod"
const API_BASE_URL = ENV == "prod" ? 'https://bpaternostro.site/fitbox/api' : "http://localhost:8000/fitbox/api";

export const ICON_SIZE_BIG = 40
export const ICON_SIZE_NORMAL = 22
export const COMPANY_NAME = "FITBOX"
export const HIGHLIGHT_COLOR = "#7315fe"
export const PASSWORD_LENGTH = 4
export const ADMIN_ROLE = "admin"
export const YOUTUBE_VIDEO_PARAMETERS_AUTOPLAY = "?autoplay=1&mute=1&controls=0&loop=1&showinfo=0&modestbranding=1&autohide=1&playlist="
export const YOUTUBE_VIDEO_PARAMETERS = "?mute=1&controls=0&showinfo=0&modestbranding=1&autohide=1&playlist="
export const ROOT = "/fitbox"
export const ROUTINE_STATUS_OK = 1
export const PHONE = 1
export const API_ENDPOINTS = {
  whatsapp: `https://wa.me/${PHONE}`,
  uploadImage: `${API_BASE_URL}/products/image-upload`,
  customers:`${API_BASE_URL}/customers`,
  customersUpdate:`${API_BASE_URL}/customers/update`,
  routineCustomersIndicator:`${API_BASE_URL}/routines-customer-indicator`,
  routines:`${API_BASE_URL}/routines`,
  list:`${API_BASE_URL}/list-values`,
  login:`${API_BASE_URL}/login/`,
  logout:`${API_BASE_URL}/logout/`,
  register:`${API_BASE_URL}/register/`,
  user:`${API_BASE_URL}/user/`,
  list:`${API_BASE_URL}/list-values/`,
  // Add more endpoints as needed
};