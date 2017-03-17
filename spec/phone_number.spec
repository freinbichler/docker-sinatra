require_relative '../phone_number'

describe PhoneNumber do
  it 'normalizes' do
    expect(PhoneNumber.new('+43-699-274872/23')).to eq('4369927487223')
  end
end
