/**
 * Validate user input
 * @return true if user input is accepted and false otherwise
 */
function validate_form() {
  let inputValue = document.getElementById("string").value;
  for (let i = 0; i < inputValue.length; i++) {
    if (inputValue[i] != "0" && inputValue[i] != "1") {
      alert("String tidak valid! Hanya diperbolehkan kombinasi 0 atau 1!");
      return false;
    }
  }
  return true;
}
