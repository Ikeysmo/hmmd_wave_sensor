#pragma once

#include "esphome/components/number/number.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class LightThresholdNumber : public number::Number, public Parented<HMMD_WAVEComponent> {
 public:
  LightThresholdNumber() = default;

 protected:
  void control(float value) override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
