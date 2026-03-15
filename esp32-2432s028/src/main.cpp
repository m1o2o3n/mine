#include <Arduino.h>
#include <TFT_eSPI.h>

namespace {
constexpr uint8_t kBacklightPin = TFT_BL;
constexpr uint8_t kLedPin = 27;
constexpr uint32_t kUiRefreshMs = 500;

TFT_eSPI tft;
uint32_t lastRefresh = 0;
bool ledState = false;

void drawStaticUi() {
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_YELLOW, TFT_BLACK);
  tft.setTextDatum(TC_DATUM);
  tft.drawString("ESP32-2432S028 Demo", 120, 12, 2);

  tft.drawRoundRect(10, 36, 220, 118, 8, TFT_DARKGREY);
  tft.setTextColor(TFT_CYAN, TFT_BLACK);
  tft.drawString("Live Status", 120, 48, 2);
}

void drawDynamicUi() {
  tft.fillRect(20, 70, 200, 72, TFT_BLACK);
  tft.setTextDatum(TL_DATUM);
  tft.setTextColor(TFT_GREEN, TFT_BLACK);
  tft.drawString(String("Uptime: ") + millis() / 1000 + " s", 24, 75, 2);
  tft.drawString(String("LED: ") + (ledState ? "ON" : "OFF"), 24, 98, 2);
  tft.drawString("Board: ESP32-2432S028", 24, 121, 2);
}
}  // namespace

void setup() {
  pinMode(kLedPin, OUTPUT);
  pinMode(kBacklightPin, OUTPUT);

  digitalWrite(kBacklightPin, HIGH);

  Serial.begin(115200);
  delay(120);
  Serial.println("Booting ESP32-2432S028 demo...");

  tft.init();
  tft.setRotation(1);

  drawStaticUi();
  drawDynamicUi();
}

void loop() {
  if (millis() - lastRefresh >= kUiRefreshMs) {
    lastRefresh = millis();
    ledState = !ledState;
    digitalWrite(kLedPin, ledState ? HIGH : LOW);
    drawDynamicUi();
  }
}
