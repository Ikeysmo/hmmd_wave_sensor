#pragma once

#include "esphome/components/select/select.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class BaudRateSelect : public select::Select, public Parented<HMMD_WAVEComponent> {
 public:
  BaudRateSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
