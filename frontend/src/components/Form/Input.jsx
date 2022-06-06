import React from 'react';
import { Controller, useFormContext } from 'react-hook-form';
import PropTypes from 'prop-types';

import { TextField } from '@mui/material';


/**
 * AutoComplete Component
 * @param {props} props props
 * @return {JSX}
 */
function Input({ type, defaultValue, label, name, control=null, width=null, ...props }) {
  const _form = useFormContext();

  if (control === undefined) {
    control = _form.control;
  }
  return (
    <>
      <Controller
        control={control}
        name={name}
        defaultValue={defaultValue ?? null}
        render={({ field: { onChange, value }, fieldState, ...props }) => (
          <TextField
            sx={{ width: width ? width : '100%' }}
            label={label}
            type={type}
            onChange={onChange}
            value={value}
            margin="normal"
            error={Boolean(fieldState.error)}
            helperText={fieldState?.error?.message}
            {...props}
          />
        )}

      />
    </>
  );
}
export default Input;

Input.propTypes = {
  control: PropTypes.object,
  label: PropTypes.string,
  name: PropTypes.string,
  width: PropTypes.number,
  defaultValue: PropTypes.string,
  type: PropTypes.string,
};
